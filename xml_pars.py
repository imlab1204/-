# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET  # XML 파싱 LIB IMPORT

# input : FDX파일 경로
# output : [Character, Dialogue] 형식의 리스트
def fdx_parsing(fdx_location = './data/not_hill.fdx'):
    tree = ET.parse(fdx_location)  # XML 파일 불러오기
    root = tree.getroot() # 루트 할당

    # root = FINAL DRAFT
    # root[0] = Content
    # root[0][0] = Paragraph
    # root[0][0][0] = Text
    dialogue_list = list()
    for idx, Paragraph in enumerate(root[0]): # Content에 포함된 모든 Paragraph에 대해
        # Character와 Dialogue 순서로 되있는 부분에 대해서
        try:
            if Paragraph.attrib['Type'] == 'Character' and root[0][idx+1].attrib['Type'] == 'Dialogue':
                # Char : Dialg 형태로 출력
                C = Paragraph[0].text   #Character  (ex : WILLIAM
                D = root[0][idx+1][0].text   #Dialogue   (ex : And what would you say...
                print('%s : %s'% (C, D))

                dialogue_list.append([C, D])  # 대화내용 모두 저장해서 리턴

        except:
            continue

    return dialogue_list