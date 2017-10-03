#include <cstdio>
#include "object.h"

int main(void) {
	Object myObject;

	myObject.type = "object";
	myObject.value = 89;
	std::cout << "myObject {type: " << myObject.type << "} {value: " << myObject.value << "}\n";
	return (0);
}
