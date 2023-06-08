#include <iostream>
#include <vector>
//Vector is dynamic
//When we try to enter an element when vector is full, the capacity of the vecot doubles
// What happens is that it creates a new vector with double the current size and copy the old vector there and then add the element
using namespace std;
int main(){
    vector<int> v;
    cout<<"Capacity= "<<v.capacity()<<endl;
    v.push_back(1);
    cout<<"Capacity= "<<v.capacity()<<endl;
    v.push_back(2);
    cout<<"Capacity= "<<v.capacity()<<endl;
    v.push_back(3);
    cout<<"Capacity= "<<v.capacity()<<endl;
    cout<<"Size= "<<v.size()<<endl;

    cout<<"Front: " << v.front()<<endl;
    cout<<"Back: " << v.back()<<endl;

    v.pop_back();   //Pop last element

    v.clear();  //Clear array
    
    vector<int> v1(5,1);
    //This means we are creating a vector of size 5 and initialize all values with value 1
    
    vector<int> last(v1);
    //This will make vector with all elements as v1

    

}