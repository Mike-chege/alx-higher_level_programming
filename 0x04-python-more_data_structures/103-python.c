#include <.h>
#include <stdio.h>

/**
 * print_python_list - Prints some basic info about Python lists
 * @p: A pointer to a Python list object
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0, size = PyList_Size(p); i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: A pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *buffer;

    printf("[*] Python bytes info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  [.] Size: %ld\n", PyBytes_Size(p));
    printf("  [.] Trying string: %s\n", PyBytes_AsString(p));

    size = PyBytes_Size(p);
    if (size > 10)
        size = 10;
    buffer = PyBytes_AsString(p);

    printf("  [.] First %ld bytes: ", size);
    for (i = 0; i < size; i++)
    {
        printf("%02x", (unsigned char)buffer[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}
