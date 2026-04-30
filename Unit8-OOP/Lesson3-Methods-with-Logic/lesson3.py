"""
=============================================================================
 UNIT 8 - LESSON 3: GroupChat Class - STARTER CODE
=============================================================================
 
 Complete the methods below based on the instructions.
 
 The GroupChat class manages members using a dictionary attribute:
     self.members = {}   # username (str) : role (str)
 
 TASKS:
 1. __init__        - Initialize chat_name and empty members dict
 2. add_member      - Add a member with their role
 3. get_member_list - Return formatted list of members (NJIT Q37 pattern)
 4. is_member       - Check if a username exists
 5. remove_member   - Safely remove a member (return True/False)
 6. get_all_usernames - Return list of all usernames
 7. get_role        - Return role or None if not found
 8. update_role     - Update a member's role (return True/False)
 9. clear_members   - Remove all members from the chat
"""


class GroupChat:
    """A group chat with members and their roles."""
    
    # ---- TASK 1: Constructor ----
    def __init__(self, chat_name):
        """
        Initialize a new group chat.
        Parameters:
            chat_name (str): Name of the chat group
        TODO: 
            - Store chat_name in self.name
            - Create an empty dictionary called self.members
        """
        self.name = chat_name
        self.members = {}
    
    
    # ---- TASK 2: add_member (modifier) ----
    def add_member(self, username, role):
        """
        Add a member with their role.
        
        Parameters:
            username (str): Member's username
            role (str): Member's role (e.g., "admin", "member", "guest")
        
        TODO:
            - Add the username: role pair to self.members dictionary
        """
        self.members[username] = role
    
    
    # ---- TASK 3: get_member_list (getter) ⭐ NJIT Q47 pattern ----
    def get_member_list(self):
        """
        Return list of formatted member strings.
        
        Format: "username - (role)"
        
        Returns:
            list[str]: List of formatted member strings
        
        TODO:
            1. Create an empty list called result
            2. Loop through self.members.items() to get username and role
            3. Append f"{username} - ({role})" to result
            4. Return result
        
        Example:
            If self.members = {"maria": "admin", "jake": "member"}
            Returns: ['maria - (admin)', 'jake - (member)']
        """
        result = []
        for username, role in self.members.items():
            result.append(f"{username} - ({role})")
        return result
    
    
    # ---- TASK 4: is_member (getter) ----
    def is_member(self, username):
        """
        Check if a username is in the chat.
        
        Parameters:
            username (str): Username to check
        
        Returns:
            bool: True if username exists, False otherwise
        
        TODO:
            - Return whether username is in self.members
            - HINT: Use the 'in' operator on the dictionary
        """
        return username in self.members
    
    
    # ---- TASK 5: remove_member (conditional modifier) ----
    def remove_member(self, username):
        """
        Remove a member if they exist.
        
        Parameters:
            username (str): Username to remove
        
        Returns:
            bool: True if removed, False if not found
        
        TODO:
            1. Check if username exists in self.members
            2. If yes: delete the entry and return True
            3. If no: return False
        
        WARNING: Never use 'del' without checking existence first!
        """
        if username in self.members:
            del self.members[username]
            return True
        return False
        
    
    
    # ---- TASK 6: get_all_usernames (getter) ----
    def get_all_usernames(self):
        """
        Return a list of all usernames in the chat.
        
        Returns:
            list[str]: List of all usernames
        
        TODO:
            - Return the keys of self.members as a list
            - HINT: Use self.members.keys() and convert to list
        """
        print(type(self.members.keys()))
        print(type(self.members.values()))
        print(type(self.members.items()))
        return list(self.members.keys())
    
    
    # ---- TASK 7: get_role (conditional getter) ----
    def get_role(self, username):
        """
        Return the role of a member.
        
        Parameters:
            username (str): Username to look up
        
        Returns:
            str or None: Role if found, None if not a member
        
        TODO:
            1. Check if username exists in self.members
            2. If yes: return the role
            3. If no: return None
        """
        if username in self.members:
            return self.members[username]
        return None
            
    
    
    # ---- TASK 8: update_role (conditional modifier) ----
    def update_role(self, username, new_role):
        """
        Update a member's role.
        
        Parameters:
            username (str): Username to update
            new_role (str): New role for the member
        
        Returns:
            bool: True if updated, False if member not found
        
        TODO:
            1. Check if username exists in self.members
            2. If yes: update the role and return True
            3. If no: return False
        """
        pass  # DELETE THIS LINE AND WRITE YOUR CODE HERE
    
    
    # ---- TASK 9: clear_members (modifier) ----
    def clear_members(self):
        """
        Remove all members from the group.
        
        TODO:
            - Clear the self.members dictionary
            - HINT: Use the .clear() method
        """
        pass  # DELETE THIS LINE AND WRITE YOUR CODE HERE


# =============================================================================
# TEST CODE - Run this to verify your implementation
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("TESTING GroupChat CLASS")
    print("=" * 60)
    
    # Create a chat
    squad = GroupChat("Study Squad")
    print(f"\n✅ Created chat: {squad.name}")
    print(f"   Initial members: {squad.members}")
    
    # Test add_member
    print("\n--- Testing add_member() ---")
    squad.add_member("maria", "admin")
    squad.add_member("jake", "member")
    squad.add_member("sam", "guest")
    print(f"   After adding: {squad.members}")
    
    # Test get_member_list
    print("\n--- Testing get_member_list() ---")
    result = squad.get_member_list()
    print(f"   Result: {result}")
    
    # Test is_member
    print("\n--- Testing is_member() ---")
    print(f"   Is 'maria' a member? {squad.is_member('maria')}")
    print(f"   Is 'bob' a member? {squad.is_member('bob')}")
    
    # Test remove_member
    print("\n--- Testing remove_member() ---")
    print(f"   Remove jake: {squad.remove_member('jake')}")
    print(f"   Remove gemici: {squad.remove_member('gemici')}")
    print(f"   Members now: {squad.members}")
    
    # Test get_all_usernames
    print("\n--- Testing get_all_usernames() ---")
    print(f"   All usernames: {squad.get_all_usernames()}")
    
    # Test get_role
    print("\n--- Testing get_role() ---")
    print(f"   Role of maria: {squad.get_role('maria')}")
    print(f"   Role of bob: {squad.get_role('bob')}")
    
    # # Test update_role
    # print("\n--- Testing update_role() ---")
    # print(f"   Promote jake to admin: {squad.update_role('jake', 'admin')}")
    # print(f"   Promote nobody: {squad.update_role('nobody', 'admin')}")
    # print(f"   Jake's new role: {squad.get_role('jake')}")

    
    # # Test clear_members
    # print("\n--- Testing clear_members() ---")
    # squad.clear_members()
    # print(f"   After clear: {squad.members}")
    
    # # Edge case: empty chat
    # print("\n--- Edge Case: Empty Chat ---")
    # empty_chat = GroupChat("Empty")
    # print(f"   get_member_list() on empty: {empty_chat.get_member_list()}")
    # print(f"   get_all_usernames() on empty: {empty_chat.get_all_usernames()}")
    # print(f"   is_member('anyone'): {empty_chat.is_member('anyone')}")
    # print(f"   get_role('anyone'): {empty_chat.get_role('anyone')}")
    # print(f"   remove_member('anyone'): {empty_chat.remove_member('anyone')}")
    
    # print("\n" + "=" * 60)
    # print("✅ ALL TESTS COMPLETE")
    # print("=" * 60)