# %%
import requests as r 
 
class Fetcher: 
    def __init__(self): 
        self.__students= r.get("https://cdn.ituring.ir/ex/users.json") .json 
    def nerds(self): 
        for sc in self.__students: 
            if sc["score"] >= 18.5: 
                return { self.__students["name"] , self.__students["last_name"] } 
             
    def sultan(self): 
        max_score = 0 
        for mx in self.__students: 
            if mx["score"] > max_score: 
                max_score = mx["score"] 
        for maxs in self.__students: 
            if maxs["score"] == max_score: 
                return tuple(self.__students["name"] , self.__students["last_name"]) 
     
    def mean(self): 
        sumof_scores = 0 
        len_scores = 0 
        for avg in self.__students: 
            sumof_scores += avg["score"] 
            len_scores += 1 
        return float(sumof_scores / len_scores) 
     
    def get_students(self): 
        result = [] 
        for student in self.__students: 
            student_info = {} 
            for key in student: 
                if key not in ['city', 'province', 'geolocation']: 
                    student_info[key] = student[key] 
            result.append(student_info) 
        return result 
             
opject = Fetcher() 
print(opject.nerds) 
print(opject.sultan) 
print(opject.mean) 
print(opject.get_students)
#%%

