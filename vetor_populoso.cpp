//Elabore um algoritmo probabilistico O(n)
//Ele recebe um inteiro k e um vetor de n números reais
//Ele deve responder se A possui ou não um elemento majoritário
//isto é, um elemento que aparece mais do que n/k vezes


#include <iostream>
#include <cstdlib>
#include <ctime>

//unsigned seed = time(0);
//srand(seed)
//rand()%n

using namespace std;

int contar(int i,int *v, int n){
	int cont = 0;

	for(int j = 0; j < n; j++){
		if(v[j] == i) cont++;
	}

	return cont;
}

int main(){
	int v[10] = {0,-2,10,3,1,-1,5,0,22,0};

	int n = 10;

	int k = 5;

	unsigned seed = time(0);

	srand(seed);
	
	for(int i = 0; i < k; i++){
		if(contar(v[rand()%n], v, n) >= n/k) cout << "Tem populoso\n";

		else cout << "Não tem populoso\n";
	}

}

