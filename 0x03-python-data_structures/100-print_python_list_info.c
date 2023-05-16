#include "Python.h"
#include <stdlib.h>

/**
 * print_python_list_info - prints info about a python list object
 * @p: pointer to generic PyObject
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	const char *e_kind = NULL;
	PyListObject *list_p = NULL;
	ssize_t size = 0;
	ssize_t i = 0;

	size = PyList_Size(p);
	list_p = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", (signed long)(list_p->allocated));
	while (i < size)
	{
		e_kind = Py_TYPE(list_p->ob_t[i])->tmp_n;
		printf("Element %ld: %s\n", i, e_kind);
		i++;
	}
}

