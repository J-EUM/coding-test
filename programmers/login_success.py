# 내풀이: 1차원배열로 변경(문제조건때문에 가능)
# def solution(id_pw, db):
#     #먼저 [id, pw]세트가 db에 있으면 로그인 성공
#     if id_pw in db:
#         return 'login'  
#     db2 = sum(db,[])    # sum(db, [])는 2차원배열을 1차원배열로 바꿔준다. 

#     # id는 알파벳+숫자이고 pw는 숫자이다. 그래서 1차원 배열로 바뀐 db2에 입력id값이 있다면 db에 해당 id가 있는것. 비번이랑 같을일은 없다.
#     # 로그인이 실패했는데 id가 존재하는거면 비밀번호가 틀린것.
#     if id_pw[0] in db2: 
#         return 'wrong pw'
    
#     # 로그인실패인데 아이디가 있지도 않은것: fail
#     return 'fail'

# 다른사람풀이: 딕셔너리
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]): 
    # dict(2차원리스트)의 결과는 리스트 각 요소의[0]을 키, [1]을 값으로 하는 딕셔너리 반환.
    # :=는 값을 평가하기 전에 할당한다. db_pw = dict(db).get(id_pw[0]) , if db_pw: 랑 같은거
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"


db = [['id', 'pw'],['id2', 'pw2']]
db2 = ['id10', 'pw10', 'id20', 'pw20']

print(db)
print(dict(db))

res = solution(['id','pw'], db)
print(res)