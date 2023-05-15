#include <Python.h>


/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: A pointer to a Python list object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	PyObject *item;

	printf("[*] Size of Python List = %ld\n", size);
	print("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", Py_TYPE(item)->tp_name);
	}
}

