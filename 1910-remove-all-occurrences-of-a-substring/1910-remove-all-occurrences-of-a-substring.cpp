class Solution {
public:
    string removeOccurrences(string s, string part) {
        
        int part_len = part.length();
        bool x = true;
        while(x){
        int part_pos = s.find(part);
        if(part_pos != string::npos){
            s.erase(part_pos,part_len);}
        else x=false;
            //,str2.length()
        }
        return s;
    }
};