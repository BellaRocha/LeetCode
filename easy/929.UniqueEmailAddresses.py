#Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
# - For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.

#If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
# - For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.

#If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.
# - For example, "m.y+name@email.com" will be forwarded to "my@email.com".

#It is possible to use both of these rules at the same time.

#Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        receives_emails = 0
        if len(emails) > 100 or len(emails) < 1:
            return 0
        for i in range(len(emails)):
            if len(emails[i]) > 100 or len(emails[i]) < 1: 
                return 0
            email_s = emails[i].split('@')
            local = email_s[0]
            domain = email_s[1]
            if (domain.count('.') == 1) and ('+' not in domain) and (local[0] != '+'):
                receives_emails += 1
        return receives_emails
    
 #Time complexity: O(n), where n is the total content of emails
 #Space complexity: O(n)
