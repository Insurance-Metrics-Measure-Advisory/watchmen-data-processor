from datetime import datetime

from watchmen.pipeline.model.pipeline import ParameterJoint, Parameter
from watchmen.pipeline.single.stage.unit.utils.units_func import get_value, get_factor
from watchmen.topic.factor.factor import Factor

YEAR_OF = 'year-of',
HALF_YEAR_OF = 'half-year-of',
QUARTER_OF = 'quarter-of',
MONTH_OF = 'month-of',
WEEK_OF_YEAR = 'week-of-year',
WEEK_OF_MONTH = 'week-of-month',
DAY_OF_MONTH = 'day-of-month',
DAY_OF_WEEK = 'weekdays'

DATE_FUNC = [YEAR_OF, HALF_YEAR_OF, QUARTER_OF, MONTH_OF, WEEK_OF_YEAR, WEEK_OF_MONTH, DAY_OF_WEEK, DAY_OF_MONTH]


def build_factor_list(factor):
    factor_name_list = factor.name.split(".")
    factor_list = []
    for name in factor_name_list:
        factor = Factor()
        factor.name = name
        factor_list.append(factor)
    return factor_list


def __convert_value_to_datetime(value):
    if type(value) == datetime:
        return value
    else:
        return datetime.fromisoformat(value)


def __run_arithmetic(arithmetic, value):
    if arithmetic == "none":
        return value
    elif arithmetic == "year-of":
        return __convert_value_to_datetime(value).year
    elif arithmetic == "month-of":
        return __convert_value_to_datetime(value).month
    elif arithmetic == "week-of":
        return __convert_value_to_datetime(value).isocalendar()[1]
    elif arithmetic == "weekday":
        return __convert_value_to_datetime(value).weekday()


def run_arithmetic_value_list(arithmetic, source_value_list):
    if type(source_value_list) == list:
        results = []
        for source_value in source_value_list:
            results.append(__run_arithmetic(arithmetic, source_value))
        return results
    else:
        return __run_arithmetic(arithmetic, source_value_list)


def run_mapping_rules(mapping_list, target_topic, raw_data, pipeline_topic):
    mapping_results = []
    for mapping in mapping_list:
        source = mapping.source
        result = []
        source_value_list = run_arithmetic_value_list(mapping.arithmetic,
                                                      get_source_value_list(pipeline_topic, raw_data, result, source))
        target_factor = get_factor(mapping.factorId, target_topic)
        mapping_results.append({target_factor.name: source_value_list})

    print(mapping_results)
    mapping_data_list = merge_mapping_data(mapping_results)
    return mapping_data_list


def __is_date_func(source_type):
    return source_type in DATE_FUNC


def __process_date_func(source):
    pass


def __is_calculation_operation(type):
    pass


def __process_compute_kind(source: Parameter):
    if __is_date_func(source.type):
        return __process_date_func(source)
    elif __is_calculation_operation(source.type):
        pass


def get_source_value_list(pipeline_topic, raw_data, result, source):
    if source.kind == "topic":
        source_factor = get_factor(source.factorId, pipeline_topic)
        return get_source_factor_value(raw_data, result, source_factor)
    elif source.kind == "constant":
        return source.value
    elif source.kind == "computed":
        __process_compute_kind(source)
        # TODO computed kind
        return []
    else:
        raise Exception("Unknown source kind {0}".format(source.kind))


def get_source_factor_value(raw_data, result, source_factor):
    if is_sub_field(source_factor):
        factor_list = build_factor_list(source_factor)
        source_value_list = get_factor_value(0, factor_list, raw_data, result)
    else:
        source_value_list = get_value(source_factor, raw_data)
    return source_value_list


def merge_mapping_data(mapping_results):
    max_value_size = get_max_value_size(mapping_results)
    mapping_data_list = []
    for i in range(max_value_size):
        mapping_data = {}
        for mapping_result in mapping_results:
            for key, value in mapping_result.items():
                if type(value) is list and len(value) > 0:
                    mapping_data[key] = value[i]
                else:
                    mapping_data[key] = value
        mapping_data_list.append(mapping_data)
    return mapping_data_list


def get_max_value_size(mapping_results):
    index = 0
    for mapping_result in mapping_results:
        for key, value in mapping_result.items():
            if type(value) is list:
                # index = len(value)
                if len(value) > index:
                    index = len(value)
            else:
                index = 1
    return index


def __process_parameter_join(parameter_join: ParameterJoint):
    if parameter_join.jointType == "and":

        pass
    elif parameter_join.jointType == "or":
        pass
    else:
        raise Exception("unknown parameter join type {0}".format(parameter_join.jointType))


def build_right_query(condition, pipeline_topic, raw_data, target_topic):
    where_condition = []
    for sub_condition in condition.filters:
        # print("sub_condition:", sub_condition)
        right_factor = get_factor(sub_condition.right.factorId, pipeline_topic)
        # print("right_factor:", right_factor)

        left_factor = get_factor(sub_condition.left.factorId, target_topic)
        # right_value = get_value(right_factor, raw_data)
        right_value_list = get_source_factor_value(raw_data, [], right_factor)
        where_condition.append(
            {"name": left_factor.name, "value": right_value_list, "operator": sub_condition.operator,
             "right_factor": right_factor})
        # left_value = get_value(sub_condition.left,target_topic_data,target_topic)
    return where_condition


def is_sub_field(factor):
    return "." in factor.name


def get_factor_value(index, factor_list, raw_data, result):
    factor = factor_list[index]
    data = get_value(factor, raw_data)
    if type(data) is list:
        for raw in data:
            get_factor_value(index + 1, factor_list, raw, result)
    elif type(data) is dict:
        get_factor_value(index + 1, factor_list, data, result)
    else:
        result.append(data)
    return result
