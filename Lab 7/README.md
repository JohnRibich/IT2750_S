5.i: You don not need to have the number of rails be greater then the message length divided by two because you want the message to evenly fit in the allotted rails. Ex: 24 chars/ 3 Rails = 8 Char per rail
5.ii: You only want to check cases where the rails evenly divide the message because it makes it so the message can evenly fit and be run through/moved around to decrypt it. 
6: wordPop Function: accepts text and length, returns list of all words that are N length
7: re.match[ing]+
8: re.match('[abc]XY.') matches words starting with a but need to find how to find ending
