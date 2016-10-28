# coding=UTF-8
import sys
import re
from PIL import Image, ImageFilter

FIRST_COL_OFFSET = 18 # Distance from left edge to center of first column
COL_GAP = 7 # Distance between columns

FIRST_ROW_OFFSET = 25 # Distance from top to center of first row
ROW_GAP = 20 # Distance between rows

COLS = 80
ROWS = 12

class PunchCardColumn:
	'''
	Symbols is a dict of symbol sets by name:
	SYMBOLS = {
		'IBM_029': {
			'100100000000': 'A',
			...
		}
	}
	Symbols are defined as column definitions
	top of column is most left in key.
	Row punches are represented in top-down order, 
	not defined row index; IE: First row of punchcard 
	is technically row 12 and 3rd row is row 0 but instead we store in 
	visual top-down order where 12 is 0, 0 is 2, and 9 is 11.
	'''	
	SYMBOLS = {}

	# Pull symbol cards from: http://homepage.divms.uiowa.edu/~jones/cards/codes.html
	# A card def must be all the same length strings, so don't trim it.
	CARDS = {
		'IBM_029': [
			u"&-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ:#@'=\"¢.<(+|!$*);¬ ,%_>?",
			u'O           OOOOOOOOO                        OOOOOO            ',
			u' O                   OOOOOOOOO                     OOOOOO      ',
			u'  O                           OOOOOOOOO                  OOOOOO',
			u'   O        O        O        O                                ',
			u'    O        O        O        O       O     O     O     O     ',
			u'     O        O        O        O       O     O     O     O    ',
			u'      O        O        O        O       O     O     O     O   ',
			u'       O        O        O        O       O     O     O     O  ',
			u'        O        O        O        O       O     O     O     O ',
			u'         O        O        O        O       O     O     O     O',
			u'          O        O        O        O OOOOOOOOOOOOOOOOOOOOOOOO',
			u'           O        O        O        O                        ',
		],
		'EBCD_029': [
			u"&-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ:#@'=\"[.<(+|]$*);^\\,%_>?",
			u'O           OOOOOOOOO                        OOOOOO            ',
			u' O                   OOOOOOOOO                     OOOOOO      ',
			u'  O                           OOOOOOOOO                  OOOOOO',
			u'   O        O        O        O                                ',
			u'    O        O        O        O       O     O     O     O     ',
			u'     O        O        O        O       O     O     O     O    ',
			u'      O        O        O        O       O     O     O     O   ',
			u'       O        O        O        O       O     O     O     O  ',
			u'        O        O        O        O       O     O     O     O ',
			u'         O        O        O        O       O     O     O     O',
			u'          O        O        O        O OOOOOOOOOOOOOOOOOOOOOOOO',
			u'           O        O        O        O                        ',
		],
		'CDC_029': [
			u"+-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ:=±<%[<.)>¬;v$*|¦>],(a=^",
			u'O           OOOOOOOOO                        OOOOOO            ',
			u' O                   OOOOOOOOO                     OOOOOO      ',
			u'  O                           OOOOOOOOO                  OOOOOO',
			u'   O        O        O        O                                ',
			u'    O        O        O        O       O     O     O     O     ',
			u'     O        O        O        O       O     O     O     O    ',
			u'      O        O        O        O       O     O     O     O   ',
			u'       O        O        O        O       O     O     O     O  ',
			u'        O        O        O        O       O     O     O     O ',
			u'         O        O        O        O       O     O     O     O',
			u'          O        O        O        O OOOOOOOOOOOOOOOOOOOOOOOO',
			u'           O        O        O        O                        ',
		]
	}

	# Build symbols from cards
	for name, data in CARDS.iteritems():
		# split the line by char
		# 'O's are punches in the card defs but we store punches as 1s
		# skip first row as it char def line
		data = [list(line) if i == 0 else list(line.replace('O','1').replace(' ','0')) for i, line in enumerate(data)]

		# flip it so each list is now a column
		data = zip(*data)

		symbol_set = {}
		for col in data:
			character = col[0]
			punches = ''.join(col[1:])
			symbol_set[punches] = character

		SYMBOLS[name] = symbol_set

	def __init__(self, rows, symbol=None, unknown_char=u'¿'):
		symbol = symbol or 'IBM_029'

		self.data = [0] * rows
		self.symbol_set = self.SYMBOLS[symbol]
		self.unknown_char = unknown_char

	def punch(self, index):
		self.data[index] = 1

	def read(self):
		key = ''.join([str(i) for i in self.data])
		character = self.symbol_set.get(key, None)
		if character is None:
			# all zero is considered a space (if not already defined as something obviously)
			character = ' ' if re.match('^0+$', key) else self.unknown_char
		return character

def isWhite(p):
	'''
	p is a pixel tuple
	'''
	THRESHOLD = 250
	return p[0] > THRESHOLD and p[1] > THRESHOLD and p[2] > THRESHOLD

def readCard(img, symbol_set=None):
	im = Image.open(img)

	# Readings will be stored in 
	# card[col]
	card = [PunchCardColumn(ROWS, symbol_set) for x in range(COLS)]

	column = 0
	# X and Y are pixel x,y
	for x in range(FIRST_COL_OFFSET, im.width, COL_GAP):
		row = 0
		for y in range(FIRST_ROW_OFFSET, im.height, ROW_GAP):
			p = im.getpixel((x,y))
			#print '%s, %s is %s : looked %s, %s' % (column,row,isWhite(p), x, y)
			if isWhite(p) and column < len(card):
				card[column].punch(row)
			row = row + 1
		column = column + 1

	return card
	
def printCard(card):
	# list of PunchCardColumns
	print ''.join([pcc.read() for pcc in card])

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'First arg should be the card image'
		sys.exit(1)

	printCard(readCard(*sys.argv[1:]))
