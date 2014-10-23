#include <iostream>
#include <map>
#include <vector>
#include <stdlib.h>
#define MAXN 100001
using namespace std;

int main(){
	int k, d;
	long long int a[MAXN], b[MAXN], c[MAXN];
	int i, index, count, diff;
	string output;
	map <int, vector<int> > dif;
	vector<int> keys;
	
	cin >> k >> d;
	
	for (i=0; i<k; i++){
		cin >> a[i];
		//b[i] = -1;
		c[i] = -1;
	}
	
	dif[0].push_back(k-1);
	keys.push_back(0);
	
	for(i=k-2; i>=0; i--){
		diff = keys.size()-1;
		index = 0;
		
		while (abs(a[i] - a[dif[keys[diff]][index]]) < d){
			index ++;
			if (index == dif[keys[diff]].size()){
				index = 0;
				diff --;
			}
			if(diff == -1){
				break;
			}
		}
		cout << i << " " << diff << " " << index << endl; 
		if(diff >= 0){
			if (dif.find(diff+1) != dif.end()){
				keys.push_back(diff+1);
			}
			dif[diff+1].push_back(i);
			c[i] = dif[keys[diff]][index];
		}
		else{
			dif[0].push_back(i);
		}
	}
	
	for(i=0; i<k; i++){
		cout << c[i] << " ";
	}
	cout << endl;
	
	for(i=0; i<keys.size(); i++){
		cout << keys[i] << " ";
	}
	cout << endl;
	
	index = dif[dif.rbegin() -> first].back();
	//cout << dif.rbegin() -> first + 1;
	cout << keys.back();
	cout << "\n";
	cout << index+1;

	while (c[index] != -1){
		cout << " ";
		cout << c[index]+1;
		index = c[index];
	}
	cout << endl;
	
	index = dif[dif.rbegin() -> first].back();
	cout << index;
	while (c[index] != -1){
		cout << " ";
		index = c[index];
		cout << index;
	}
	
		
}