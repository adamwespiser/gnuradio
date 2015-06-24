#ifndef _errors_h
#define _errors_h


#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#ifdef DEBUG
# define DPRINTF(arg) printf arg
#else
# define DPRINTF(arg)
#endif


#define err_abort(code,text) do { \
		fprintf (stderr, "%s at \"%s\":%d: %s\n", \
						text, __FILE__, __LINE__, strerror (code)); \
		abort (); \
		} while (0)

#define errno_abort(text) { \
		fprintf (stderr, "%s at \"%s\":%d: %s\n", \
						text, __FILE__, __LINE__, strerror (errno)); \
		abort(); \
		} while (0)
#endif



