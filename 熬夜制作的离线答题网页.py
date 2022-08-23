#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: fuutianyii
Date: 2022-08-21 18:44:07
LastEditors: fuutianyii
LastEditTime: 2022-08-22 18:10:09
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''

'''
                  ___====-_  _-====___
            _--^^^#####//      \\#####^^^--_
         _-^##########// (    ) \\##########^-_
        -############//  |\^^/|  \\############-
      _/############//   (@::@)   \############\_
     /#############((     \\//     ))#############\
    -###############\\    (oo)    //###############-
   -#################\\  / VV \  //#################-
  -###################\\/      \//###################-
 _#/|##########/\######(   /\   )######/\##########|\#_
 |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
 `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
    `   `  `      `   / | |  | | \   '      '  '   '
                     (  | |  | |  )
                    __\ | |  | | /__
                   (vvv(VVV)(VVV)vvv)

     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               神兽保佑            永无BUG
'''

import hashlib
def arrange_data(file):
    f=open(file,"rb")
    exam_list=f.readlines()
    # print(exam_list)
    exam_dict={}
    continue_it=False
    for rowid in range(0,len(exam_list)):
        if continue_it==False:
            exam_list[rowid]=exam_list[rowid].replace(b"\r\n", b"").replace(b"\n", b"")
            exam_list[rowid]=exam_list[rowid].decode()
            exam_list[rowid+1]=exam_list[rowid+1].replace(b"\r\n", b"").replace(b"\n", b"")
            exam_dict[str((rowid+2)//2)+"."+exam_list[rowid]]=exam_list[rowid+1]
            continue_it=True
        else:
            continue_it=False
            continue
    return exam_dict

def encode_data(exam_dict):
    for (p,a) in exam_dict.items():
        exam_dict[p]=hashlib.md5(exam_dict[p]).hexdigest()
    answerlist=[]
    for md5 in exam_dict.values():
        answerlist.append(md5)
    return exam_dict,answerlist

def make_input(exam_dict):
    data=""
    id=1
    for key in exam_dict.keys():
        data+=f"""{key}\n<br><input type="text" class="input" onkeydown="press_enter(event);" id="{id}">\n<br>"""
        id+=1
    return data


if __name__ == "__main__":
    exam_dict=arrange_data("题目.txt")
    # print(len(exam_dict))
    (exam_dict,answerlist)=encode_data(exam_dict)
    # print(len(exam_dict))
    # print(answerlist)
    input_code=make_input(exam_dict)
    f=open("测试.html","w",encoding="utf-8")
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>悲哀的工具人发布的测试</title>
    <style>
        #main{
            margin: auto;
            width: 700px;
        }
        .input{
            font-size:20px;
            /* 设置输入框中字体的大小 */
            height:40px; 
            width: 100%;
            /* 设置输入框的高度 */
            border-radius:4px; 
            /* 设置输入框的圆角的大小 */
            border:1px solid #c8cccf;
            /* 设置输入框边框的粗细和颜色 */
            color:#986655; 
            /* 设置输入框中文字的颜色 */
            outline:0; 
            /* 将输入框点击的时候出现的边框去掉 */
            text-align:left; 
            /* 设置输入框中文字的位置 */
            padding-left: 10px;
            display:block; 
            /* 将输入框设置为块级元素 */
            cursor: pointer;
            box-shadow: 2px 2px 5px 1px #ccc;  
        }

        .right{
            color:green; 
        }
    </style>
    <script src="MD5.js"></script>
</head>
<body>
    <div id="main">
        <h2>score:<span id="score">0</span></h2>
        <h2>程序新鲜出炉，自行备份，一切问题与熬夜敲代码的工具人无关！</h2>
        """+input_code+"""
    </div>
</body>
<script>
(function(){
    var answerlist="""+str(answerlist)+"""
    for(var i = 0; i < localStorage.length; i++) {
        input=document.getElementById(localStorage.key(i))
        if (md5(localStorage.getItem(localStorage.key(i)))==answerlist[localStorage.key(i)-1])
        {
            document.getElementById("score").innerText=Number(document.getElementById("score").innerText)+1
            input.className="input right"
            input.value="绝密答案"
            input.disabled=true
        }
    }            
})()
// 按下enter键，发送请求，回车键的键值为13
function press_enter(e){
    var answerlist="""+str(answerlist)+"""
    var evt = window.event || e;
    if (evt.keyCode == 13){
        if (answerlist[e.target.id-1] == md5(e.target.value))
        {
            var input =document.getElementById(e.target.id)
            input.className="input right"
            document.getElementById("score").innerText=1+Number(document.getElementById("score").innerText)
            localStorage.setItem(e.target.id,e.target.value);
            document.getElementById(e.target.id).value="绝密答案"
            input.disabled=true
        }
        else{
            document.getElementById(e.target.id).value=""
        }
    }
    }
</script>
</html>""")
    f.close()