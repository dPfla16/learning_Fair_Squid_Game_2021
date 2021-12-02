# 오징어 게임 시작
print('오징어 게임에 참가자 여러분을 환영합니다. 시작하겠습니다.')
print(' ')

#0단계 번호부여
import random
num = str(random.randint(1, 456))
print('당신의 참가번호는' + ' ' + num + '번 입니다.')
print(' ')

#1단계 무궁화 꽃이 피었습니다
print('첫 번째 게임은 "무궁화 꽃이 피었습니다."입니다.')
print('술래가 수식을 외치는 동안 전진할 수 있으며, 이후 답안이 감지되지 않거나 오답이 감지되면 탈락입니다.')
print('세 문제 안에 오답을 피해 결승선에 들어오시는 분들은 통과입니다.')
print(' ' )

Ans1 = input('240 + 067 = ')
if Ans1 == '307':
    print('정답입니다.')

    Ans2 = input('218 - 199 = ')
    if Ans2 == '19':
        print('정답입니다.')

        Ans3 = input('456 X 2 = ')
        if Ans3 == '912':
            print( num + '번 참가자 통과. 축하드립니다. 다음 단계로 이동합니다.')
            print('')
#2단계 별사탕 뽑기
            print('두 번째 게임에 오신 참가자 여러분을 환영합니다.')
            print('게임을 시작하기 전에 다음 세 가지 모양 중 하나를 선택해 입력하세요.')
            choice = input('triangle, square, circle :')

            if choice == 'triangle' :
                print("*"*8)
                s = int(7)
                for i in range(1,s):
                    print("*" +" " * (i) + "*" * (1 * (s-i)))
                print("*"*8)
                print ('두 번째 게임은 "별사탕 뽑기"입니다.')
                choicetri = input('선택하신 모양에 쓰인 *의 개수를 맞추면 통과입니다. 개수는?:')
                if choicetri == '43':
                    print(num+'번 참가자 통과. 다음 단계로 이동합니다.')
                    print('')
#3단계 징검다리 건너기
                    print('마지막 게임에 오신 참가자 여러분을 환영합니다.')
                    print('마지막 게임은 "징검다리 건너기"입니다.')
                    print('한 쌍의 좌, 우 다리 중에 어느 쪽이 정답인지를 판단해서')
                    print('답을 입력하고 다섯 쌍의 다리를 무사히 건너가면 통과입니다. 그럼 시작합니다.')

                    Jin1 = input('좌 or 우 :')
                    if Jin1 == '우':
                        print('다음 다리를 선택해 주세요.')
    
                        Jin2 = input('좌 or 우 :')
                        if Jin2 == '우':
                            print('다음 다리를 선택해 주세요.')
        
                            Jin3 = input('좌 or 우 :')
                            if Jin3 == '좌':
                                print('다음 다리를 선택해 주세요.')

                                Jin4 = input('좌 or 우 :')
                                if Jin4 == '좌':
                                    print('다음 다리를 선택해 주세요.')
                
                                    Jin5 = input('좌 or 우 :')
                                    if Jin5 == '우':
                                        print( num + '번 참가자 축하합니다. 모든 단계를 통과하였습니다. ')
                                    
                                    else :
                                        print(num +'번 참가자 탈락')
                                        print('게임을 종료합니다.')
                                else :
                                    print( num +'번 참가자 탈락')
                                    print('게임을 종료합니다.')
                            else :
                                print( num +'번 참가자 탈락')
                                print('게임을 종료합니다.')
                        else :
                            print( num +'번 참가자 탈락')
                            print('게임을 종료합니다.')
                    else :
                        print( num+'번 참가자 탈락')
                        print('게임을 종료합니다.')
                else :
                    print(num +'번 참가자 탈락')
                    print('게임을 종료합니다.')


            elif choice == 'square' :
                s = int(4)
                for i in range(1, s +1):
                    print("*" * (2 * (s-i) +1) + " " * (2 * (i-1)) + " " * (2 * (i-1)) + "*" * (2 * (s-i) +1))

                for j in range(1,s):
                    print("*" * ((2 * j) +1) + " " * (2 * (s-j-1)) + " " * (2 * (s-j-1)) + "*" * ((2 * j) +1))
                print ('두 번째 게임은 "별사탕 뽑기"입니다.')
                choicesqu = input('선택하신 모양에 쓰인 *의 개수를 맞추면 통과입니다. 개수는?: ')
                if choicesqu == '62':
                    print(num+'번 참가자 통과. 다음 단계로 이동합니다.')
                    print('')
                    print('마지막 게임에 오신 참가자 여러분을 환영합니다.')
                    print('마지막 게임은 "징검다리 건너기입니다."')
                    print('한 쌍의 좌, 우 다리 중에 어느 쪽이 정답인지를 판단해서')
                    print('답을 입력하고 다섯 쌍의 다리를 무사히 건너가면 통과입니다. 그럼 시작합니다.')
                    Jin1 = input('좌 or 우 :') 
                    if Jin1 == '우':
                        print('다음 다리를 선택해 주세요.')
    
                        Jin2 = input('좌 or 우 :')
                        if Jin2 == '우':
                            print('다음 다리를 선택해 주세요.')
        
                            Jin3 = input('좌 or 우 :')
                            if Jin3 == '좌':
                                print('다음 다리를 선택해 주세요.')

                                Jin4 = input('좌 or 우 :')
                                if Jin4 == '좌':
                                    print('다음 다리를 선택해 주세요.')
                
                                    Jin5 = input('좌 or 우 :')
                                    if Jin5 == '우':
                                        print( num + '번 참가자 축하합니다. 모든 단계를 통과하였습니다. ')
                                    
                                    else :
                                        print(num +'번 참가자 탈락')
                                        print('게임을 종료합니다.')
                                else :
                                    print( num +'번 참가자 탈락')
                                    print('게임을 종료합니다.')
                            else :
                                print( num +'번 참가자 탈락')
                                print('게임을 종료합니다.')
                        else :
                            print( num +'번 참가자 탈락')
                            print('게임을 종료합니다.')
                    else :
                        print( num+'번 참가자 탈락')
                        print('게임을 종료합니다.')
                else :
                    print(num +'번 참가자 탈락')
                    print('게임을 종료합니다.')
                           

            elif choice =='circle' :
                for i in range(3, 8):
                    for j in range(1, i+2):
                        print('*', end='')
                    print()
                for i in range(8, 3, -1):
                    for j in range(1, i+1):
                        print('*', end='')
                    print()
                print ('두 번째 게임은 "별사탕 뽑기"입니다.')
                choicecir = input('선택하신 모양에 쓰인 *의 개수를 맞추면 통과입니다. 개수는?: ')

                if choicecir == '60' :  
                    print(num+'번 참가자 통과. 다음 단계로 이동합니다.')
                    print('')
                    print('마지막 게임에 오신 참가자 여러분을 환영합니다.')
                    print('마지막 게임은 "징검다리 건너기"입니다.')
                    print('한 쌍의 좌, 우 다리 중에 어느 쪽이 정답인지를 판단해서')
                    print('답을 입력하고 다섯 쌍의 다리를 무사히 건너가면 통과입니다. 그럼 시작합니다.')

                    Jin1 = input('좌 or 우 :') 
                    if Jin1 == '우':
                        print('다음 다리를 선택해 주세요.')
    
                        Jin2 = input('좌 or 우 :')
                        if Jin2 == '우':
                            print('다음 다리를 선택해 주세요.')
        
                            Jin3 = input('좌 or 우 :')
                            if Jin3 == '좌':
                                print('다음 다리를 선택해 주세요.')

                                Jin4 = input('좌 or 우 :')
                                if Jin4 == '좌':
                                    print('다음 다리를 선택해 주세요.')
                
                                    Jin5 = input('좌 or 우 :')
                                    if Jin5 == '우':
                                        print( num + '번 참가자 축하합니다. 모든 단계를 통과하였습니다. ')
                                    
                                    else :
                                        print(num +'번 참가자 탈락')
                                        print('게임을 종료합니다.')
                                else :
                                    print( num +'번 참가자 탈락')
                                    print('게임을 종료합니다.')
                            else :
                                print( num +'번 참가자 탈락')
                                print('게임을 종료합니다.')
                        else :
                            print( num +'번 참가자 탈락')
                            print('게임을 종료합니다.')
                    else :
                        print( num+'번 참가자 탈락')
                        print('게임을 종료합니다.')
                else :
                    print(num +'번 참가자 탈락')
                    print('게임을 종료합니다.')
            else :
                print(num +'번 참가자 탈락')
                print('게임을 종료합니다.')
        else :
            print(num + '번 참가자 탈락')
            print('게임을 종료합니다.')
    else :
        print(num + '번 참가자 탈락')
        print('게임을 종료합니다.')
else :
    print(num + '번 참가자 탈락')
    print('게임을 종료합니다.')
 


                
