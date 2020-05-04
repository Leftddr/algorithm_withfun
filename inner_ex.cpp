#include <iostream>
#include <stdio.h>
using namespace std;

class Outer{
    public:
        class Inner{
            public:
                int InnerData;
                Inner(int _data) {InnerData = _data + 50;}
        };
    public:
        Outer(int _data) : m_Inner(_data)
        {
            m_OutData = _data;
        }

        void print(){
            printf("OutData : %d, InnerData : %d\n", m_OutData, m_Inner.InnerData);
        }
    private:
        Inner m_Inner;
        int m_OutData;
};

int main(int argc, char* argv[]){
    Outer outer(5);
    outer.print();

    vector<int> v(5, 0);

    cout << v[0] << '\n';
    cout << v[1] << '\n';

    
}