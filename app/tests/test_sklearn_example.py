import app_ml_basic.sklearn_example as sk_exam


def test_init_test():
    assert sk_exam.init_test() == "sklearn_exam_test"


def test_fn_load_breast_cancer():
    sk_exam.fn_load_breast_cancer()


def test_fn_decision_tree():
    sk_exam.fn_decision_tree()
