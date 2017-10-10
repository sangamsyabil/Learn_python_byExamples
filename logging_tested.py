# Code written by : Hem Raj Regmi (sangamsyabil@gmail.com) http://hemrajregmi.com

# Logging modules in python (example to solve a quadratic equation using logging)
# Logging module purpose: record progresses and problems

import logging
import math

# Create and configure logger
LOG_FORMAT = "%(levelname)s, %(asctime)s - %(message)s"
logging.basicConfig(filename = "C:\\python_log_file\\logfile.log", level=logging.DEBUG, format=LOG_FORMAT, filemode='w')
logger = logging.getLogger()

def quadratic_formula(a,b,c):
    """return the solution of equation a*x**2 + b*x + c = 0"""
    logger.info("quadratic_formula ({0}, {1}, {2})".format(a, b, c))

    # Compute the discriminant
    logger.debug("Compute the discriminant")
    disc = b**2 - 4*a*c

    # Compute the roots
    logger.debug("Compute two roots")
    root1 = (-b + math.sqrt(disc))/(2*a)
    root2 = (-b - math.sqrt(disc))/(2*a)

    # Return two roots as tuples
    logger.debug("Return two roots")
    return (root1, root2)

q_roots = quadratic_formula(1,0,-4)
print(q_roots)

# Happy code monitoring !!!





