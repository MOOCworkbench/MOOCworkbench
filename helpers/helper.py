from experiments_manager.helper import verify_and_get_experiment
from experiments_manager.models import Experiment
from marketplace.models import InternalPackage
from helpers.helper_mixins import ExperimentPackageTypeMixin


def get_package_or_experiment(request, object_type, object_id):
    if object_type == ExperimentPackageTypeMixin.EXPERIMENT_TYPE:
        return verify_and_get_experiment(request, object_id)
    elif object_type == ExperimentPackageTypeMixin.PACKAGE_TYPE:
        return InternalPackage.objects.get(id=object_id)


def get_package_or_experiment_without_request(object_type, object_id):
    if object_type == ExperimentPackageTypeMixin.EXPERIMENT_TYPE:
        return Experiment.objects.get(pk=object_id)
    elif object_type == ExperimentPackageTypeMixin.PACKAGE_TYPE:
        return InternalPackage.objects.get(id=object_id)
