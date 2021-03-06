from coverage_manager.helpers.coveralls_helper import CoverallsHelper
from git_manager.helpers.github_helper import GitHubHelper
from quality_manager.measurements.measurement import MeasurementAbstraction
from quality_manager.models import (ExperimentMeasure, ExperimentMeasureResult,
                                    RawMeasureResult)


class TestMeasurement(MeasurementAbstraction):
    def __init__(self, experiment_step):
        super().__init__(experiment_step)
        self.measurement = ExperimentMeasure.objects.get(name='Testing')
        self.github_helper = GitHubHelper(self.experiment.owner, self.experiment.git_repo.name)
        self.raw = RawMeasureResult()

    def measure(self):
        code_coverage = self.measure_code_coverage()
        if code_coverage:
            code_coverage = float(code_coverage)

            self.raw.key = 'code_coverage'
            self.raw.value = code_coverage

            if code_coverage < 50:
                self.result.result = ExperimentMeasureResult.LOW
            elif code_coverage < 80:
                self.result.result = ExperimentMeasureResult.MEDIUM
            elif code_coverage >= 80:
                self.result.result = ExperimentMeasureResult.HIGH
        else:
            self.result.result = ExperimentMeasureResult.LOW

    def measure_code_coverage(self):
        coveralls = CoverallsHelper(user=self.github_helper.owner, repo_name=self.github_helper.repo_name)
        return coveralls.code_coverage_data()

    def save_and_get_result(self):
        self.result.measurement = self.measurement
        self.result.save()
        if self.raw.key:
            self.raw.save()
            self.result.raw_values.add(self.raw)
            self.result.save()
        return self.result
