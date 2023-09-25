class Solution(object):
    
    def clean_email(self, each_email):
        local, domain = each_email.split("@")
        local = local.split("+")[0]
        local = local.replace(".","")
        final_email = local+"@"+domain
        return final_email
    
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        clean_email_list = []
        for each_email in emails:
            clean_email = self.clean_email(each_email)
            if(clean_email not in clean_email_list):
                clean_email_list.append(clean_email)
        return len(clean_email_list)
        