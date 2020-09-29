import numpy as np

from src.errors import InvalidInput


def numpy_isclose(true_values, student_values):
    try:
        student = np.array(student_values)
    except BaseException as e:
        raise InvalidInput(e.args)

    if true_values.shape != student.shape:
        raise InvalidInput(
            "Dimensions does not match. "
            f"Expected: {true_values.shape}, Given: {student.shape}")

    result = np.isclose(student, true_values)
    status = int(np.all(result))
    comments = f"{result.sum() / result.size}% correct"

    # correct: correct or fail
    # comments: where it failed or text comments
    return status, result.tolist(), comments
