//Verificar usando algoritmos probabilisticos se duas funções polinomiais são iguais


#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int func1(int x){
	return (x+1)*(x-2)*(x+3);
}


int func2(int x){
	return x*x*x + 2*x*x - 5*x; 
}


int main(){
	unsigned seed = time(0);
	srand(seed);

	int d = 3;
	
	int r;
	int k = 3;

	for(int i = 0; i < k; i++){
		r = rand()%(100*d);

		if(func1(r) == func2(r)) cout << "São iguais\n";

		else cout << "Não são iguais\n";
	}
}
