#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: A pointer to a Python bytes object
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;
	int length, allocation, i;
	const char *type;

	length = var->ob_size;
	allocation = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", allocation);

	for (i = 0; i < length; i++)
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
	unsigned char i, length;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		length = 10;
	else
		length = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", length);
	for (i = 0; i < length; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (length - 1))
			printf("\n");
		else
			printf(" ");
	}
}

