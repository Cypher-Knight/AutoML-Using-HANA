from hana_automl.automl import AutoML
from .cache import SessionState

session_state = SessionState(
    show_results=False, train=False, automl=AutoML(None), cc=None
)
