#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 * print_python_list - Prints some basic info about Python lists
 * @p: A pointer to a Python list object
 */
void print_python_list(PyObject *p)
{
       	PyListObject *py_lst = (PyListObject *)p;
       	PyVarObject *var = (PyVarObject *)p;
	int length, allocation, i;
	const char *l_kind;

	allocation = py_lst->allocated;
	size = var->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", allocation);

	for (i = 0; i < length; i++)
	{
		l_kind = py_lst->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, l_kind);
		if (strcmp(l_kind, "bytes") == 0)
			print_python_bytes(py_lst->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p:A pointer to a python bytes object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *n_bytes = (PyBytesObject *)p;
	unsigned char i, length;

	printf("[.] Python bytes info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  Size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  Trying string: %s\n", n_bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		length = 10;
	else
		length = ((PyVarObject *)p)->ob_size + 1;

	printf("  First %d bytes: ", length);
	for (i = 0; i < length; i++)
	{
		printf("%02hhx", n_bytes->ob_sval[i]);
		if (i == (length - 1))
			printf("\n");
		else
			printf(" ");
	}
}

