def solution(id_pw, db):
    #먼저 [id, pw]세트가 db에 있으면 로그인 성공
    if id_pw in db:
        return 'login'  
    db2 = sum(db,[])    # sum(db, [])는 2차원배열을 1차원배열로 바꿔준다. 

    # id는 알파벳+숫자이고 pw는 숫자이다. 그래서 1차원 배열로 바뀐 db2에 입력id값이 있다면 db에 해당 id가 있는것. 비번이랑 같을일은 없다.
    # 로그인이 실패했는데 id가 존재하는거면 비밀번호가 틀린것.
    if id_pw[0] in db2: 
        return 'wrong pw'
    
    # 로그인실패인데 아이디가 있지도 않은것: fail
    return 'fail'
