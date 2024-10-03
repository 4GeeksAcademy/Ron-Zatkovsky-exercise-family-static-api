
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {   
                'id':0,
                'first_name':'John',
                'age':33,
                'lucky_numbers': [7, 13, 22]
            },
            {   
                'id':1,
                'first_name':'Jane',
                'age':35,
                'lucky_numbers': [10,14,3]
            },
            {   
                'id':2,
                'first_name':'Jimmy',
                'age':5,
                'lucky_numbers': [1]
            }
            ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(3, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member)

    def edit_member(self,id,body):
        for (i,obj) in enumerate(self._members):
            if id==obj['id']:
                self._members[i]=body
    def validate_id(self,id):
        for obj in self._members:
            if(obj['id']==id):
                return True
        return False

    def delete_member(self, id):
        # fill this method and update the return
        for (i,obj) in enumerate(self._members):
            if(id==obj['id']):
                self._members.pop(i)
                return "Success"
        return "Failed"

    def get_member(self, id):
        # fill this method and update the return
        for obj in self._members:
            if(obj['id']==id):
                return obj
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
