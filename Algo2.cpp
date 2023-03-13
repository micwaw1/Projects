#include <iostream>
#include <stdlib.h>
#include <cstdlib>

using namespace std;
template <typename T>

class Array {
    T* arr;
    int size;
    int nr_elements;
    int increase;

public:
    Array() {
        arr = new T[size];
        size = 1;
        nr_elements = 0;
        increase = 2;//capacity
    }
    ~Array() {
        delete[] arr;
    }

    void addElement(const T& element) { //dodawanie elementu
        if (nr_elements == size) {

            T* arr_temp;
            arr_temp = new T[size * increase];


            for (int i = 0; i < size; i++) {
                arr_temp[i] = arr[i];
            }

            arr = arr_temp;
            size = size * increase;
        }
        arr[nr_elements] = element;
        nr_elements++;
    }

    T getElement(int index) { //zworcenie danych
        if (index < 0 || index >= nr_elements) {
            return T{};
        }
        return arr[index];
    }

    int getCapacity() {
        return size;
    }

    void to_string() {
        for (int i = 0; i < nr_elements; i++) {
            cout << arr[i] << endl;
        }
    }

    void clear() {
        delete[] arr;
        arr = NULL;
        nr_elements = 0;


        size = 1;
        arr = new T[size];
        nr_elements = 0;
        increase = 2;
    }

    void print(int index) {
        T* arr_temp;
        arr_temp = new T[size];
        cout << arr[index] << endl;
    }

    void swap_elements(int index, T& value) {//podmiana elementu tab
        if (index<0 || index>nr_elements - 1) {
            cout << "Wrong index!" << endl;
        }
        else {
            arr[index] = value;
            cout << "Index: " << index << ", value: " << value << endl;
        }
    }
};

int main() {
    Array<int> f1;
    f1.addElement(7);
    cout << "capacity= " << f1.getCapacity() << endl;
    f1.addElement(19);
    cout << "capacity= " << f1.getCapacity() << endl;
    f1.addElement(44);
    cout << "capacity= " << f1.getCapacity() << endl;

    f1.to_string();
    return 0;



}