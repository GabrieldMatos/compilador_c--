programa

int soma(int a, int b){
    return a + b;
}

int maior(float a, float b){
    if(a >= b){
        return a;
    }
    else{
        b;
    }
}

int main(){
    int x = 0;
    int y = 3;
    int soma = 0;
    while(x <= y){
        soma = soma + maior(x, y);
        x = x + 1;
    }
    return 0;
}