

class Solution {
public:
    string reverseWords(string s) {
        vector<string> words; 
        string temp;
        for(int i=0;i<s.length();i++){
            cout << i << s[i] << endl;
            if(!isspace(s[i])) temp.push_back(s[i]);
            else{
                if(!temp.empty()) words.push_back(temp);
                temp = "";      }
        }
        if(!temp.empty()) words.push_back(temp);
        int j=0;
        int e=words.size()-1;
        while(j<e){
            swap(words[j],words[e]);
            j++;e--;
        }
        string news = "";
        for(int k=0;k<words.size();k++){
            news.append(words[k]);
            if(k!=words.size()-1) news.append(" ");
        }
        return news;
    }
};