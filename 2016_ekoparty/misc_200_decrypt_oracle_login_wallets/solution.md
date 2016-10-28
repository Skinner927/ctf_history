#Challenge 
All my passwords are safely stored, or not?

Attachment
misc200_87229453a454b44d.zip

#Solution
misc200_87229453a454b44d.zip extracts ekochall.rar

run `rar lt ekochall.rar`

or mac `unrar lt ekochall.rar`

```
UNRAR 3.90 beta 2 freeware      Copyright (c) 1993-2009 Alexander Roshal

By Hugo@ekodesktop

Archive ekochall.rar

 Name             Size   Packed Ratio  Date   Time     Attr      CRC   Meth Ver
               Host OS    Solid   Old
-------------------------------------------------------------------------------
Data header type: CMT
 CMT                18       31 172% 00-00-80 00:00   .....B   2AF101BF m3a 2.9
              Win95/NT       No   No
Comment: By Hugo@ekodesktop

 cwallet.sso      3981     3981 100% 07-10-16 23:13  .....A.   21A2D217 m0b 2.9
              Win95/NT       No   No
 ewallet.p12      3904     3904 100% 07-10-16 23:13  .....A.   0F2C4F8A m0b 2.9
              Win95/NT       No   No
 ekochall            0        0   0% 07-10-16 23:09  .D.....   00000000 m0  2.0
              Win95/NT       No   No
-------------------------------------------------------------------------------
    3             7885     7885 100%

    3             7885     7885 100%
listing complete
```

Important takeaway is `Hugo@ekodesktop`

Clone repo: https://github.com/tejado/ssoDecrypt and build it per instructions.

`javac -cp .:libs/:libs/bcprov-jdk16-145.jar ssoDecryptor.java`

Note the username and machine we got from the rar comment. This would not work otherwise. 

`java -cp .:libs/:libs/bcprov-jdk16-145.jar ssoDecryptor ../ekochall/cwallet.sso Hugo ekodesktop`


WIN:

```
sso key: a252ece7d911fa0e
sso secret: 0e6b16ac78d6231bd237e71e0bb931c53765a6bf8f356acd
obfuscated password: 444a4f701601137b7447745039566b03
p12 password (hex): 2b416f615a571a645f442766103d2334
--------------------------------------------------------
----------------------------------------------
Credential #1: ekoparty/EKO{vPgsSHXO0LiHlZk667Xr}@ekoparty
```