#include <Python.h>
#include <stdlib.h>

/**
 * print_python_list_info - prints information about a python list object
 * @p: pointer to generic PyObject
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	const char *e_kind = NULL;
	PyListObject *item = NULL;
	ssize_t size = 0;
	ssize_t j = 0;

	size = PyList_Size(p);
	item = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", (signed long)(item->allocated));
	while (j < size)
	{
		e_kind = Py_TYPE(size->ob_item[j])->tp_name;
		printf("Element %ld: %s\n", j, e_kind);
		j++;
	}
}

