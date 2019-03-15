# -*-coding=utf-8-*-
 
import os
import re
import io
import file_operate

top_dir = "I:\\WorkSpace\\WorkSpace_python\\mypack2.0_pycharm\\tmp\\funcell_korea\\175.10097\\tempRFile\\gen\\com\\funcell123\\relic\\kr\\google\\R-test.java"
 
# 状态
S_INIT              = 0
S_SLASH             = 1
S_BLOCK_COMMENT     = 2
S_BLOCK_COMMENT_DOT = 3
S_LINE_COMMENT      = 4
S_STR               = 5
S_STR_ESCAPE        = 6
 
def trim_dir(path):
    print("目录：" + path)
    trim_file(top_dir)

 
def trim_file(path):
    bak_file = path + ".bak"
#     os.rename(path, bak_file)
    file_operate.copyFile(path, bak_file)
    fp_src = open(bak_file)
    fp_dst = open(path, 'w')
    state = S_INIT
    for line in fp_src.readlines():
        for c in line:
            if state == S_INIT:
                if c == '/':
                    state = S_SLASH
                elif c == '"':
                    state = S_STR
                    fp_dst.write(c)
                else:
                    fp_dst.write(c)
            elif state == S_SLASH:
                if c == '*':
                    state = S_BLOCK_COMMENT
                elif c == '/':
                    state = S_LINE_COMMENT
                else:
                    fp_dst.write('/')
                    fp_dst.write(c)
            elif state == S_BLOCK_COMMENT:
                if c == '*':
                    state = S_BLOCK_COMMENT_DOT
            elif state == S_BLOCK_COMMENT_DOT:
                if c == '/':
                    state = S_INIT
                else:
                    state = S_BLOCK_COMMENT
            elif state == S_LINE_COMMENT:
                if c == '\n':
                    state = S_INIT
            elif state == S_STR:
                if c == '\\':
                    state = S_STR_ESCAPE
                elif c == '"':
                    state = S_INIT
                    fp_dst.write(c)
            elif state == S_STR_ESCAPE:
                # 这里未完全实现全部序列，如\oNNN \xHH \u1234 \U12345678，但没影响
                state = S_STR 
                fp_dst.write(c)
    fp_src.close()
    fp_dst.close()
    file_operate.delete_file_folder(bak_file)
    
# trim_dir(top_dir)
