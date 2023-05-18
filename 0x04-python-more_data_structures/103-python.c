/*
 * You are not allowed to use the following macros/functions:

    Py_SIZE
    Py_TYPE
    PyList_GetItem
    PyBytes_AS_STRING
    PyBytes_GET_SIZE
*/
#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: A pointer to a Python bytes object
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
        PyVarObject *var = (PyVarObject *)p;
	int size, alloc, i;
	const char *type;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: A pointer to a Python bytes object
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	unsigned char i, size;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

