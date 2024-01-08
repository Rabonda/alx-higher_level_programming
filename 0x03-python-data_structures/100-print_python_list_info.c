#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t ssizeP, alloc;
	PyObject *elem;

	ssizeP = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", ssizeP);
	printf("[*] Allocated = %ld\n", alloc);
	for (Py_ssize_t x = 0; x < ssizeP; x++)
	{
		elem = PyList_GET_ITEM(p, x);
		printf("Element %ld: %s\n", x, elem->ob_type->tp_name);
	}
}
