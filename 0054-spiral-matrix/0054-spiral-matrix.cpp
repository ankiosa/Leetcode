class Solution {


    
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int nrows = matrix.size();
        int ncols = matrix[0].size();
        int count = 0;
        int total = nrows*ncols;
        int row_start = 0;int row_end = nrows-1;
        int col_start = 0;int col_end = ncols-1;
        vector <int> ans;
        
        while(count<total){
            for(int i=col_start;i<=col_end;i++){
                ans.push_back(matrix[row_start][i]);
                count++;}
            row_start += 1;
            
        if(count<total){ 
            for(int j=row_start;j<=row_end;j++){ 
                ans.push_back(matrix[j][col_end]);
                count++;}}
            col_end -= 1;
        if(count<total){
            for(int k=col_end;k>=col_start;k--){ 
                ans.push_back(matrix[row_end][k]);
                count++;}}
            row_end -= 1;

        if(count<total){
            for(int l=row_end;l>=row_start;l--){ 
                ans.push_back(matrix[l][col_start]);
                count++;}
            col_start += 1;}}
        return ans;
    }
};