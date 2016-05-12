#include <iostream>
#include <vector>
#include <cstring>
#include <iterator>
#include <algorithm>
using namespace std;

void compute_prefix_function(const char *s, vector<int> &pi)
{
int k=0;
int N = strlen(s);
pi.resize(N);
for (int i=1; i!=N; ++i){
	while(k>0 && s[i] != s[k]) k = pi[k-1];
	if (s[k] == s[i]) ++k;
	pi[i] = k;
}
copy(pi.begin(), pi.end(), ostream_iterator<int>(cout, " "));
cout<<endl;
}

void kmp(const char *s, const char *p)
{
cout << "matching string " << s << " with pattern " << p <<endl;

vector<int> pi;
compute_prefix_function(s, pi);

int k=0;
for (int i=0; i!=strlen(s); ++i){
	while (k>0 && s[i]!=p[k]) k = pi[k-1];
	if (s[i] == p[k]) ++k;
	if (k == strlen(p)) cout << "matched at " << i-k+1 << " in " << s << endl;	
}
}

int main()
{
vector<int> pi;
kmp("abababcababc", "aba");
}
