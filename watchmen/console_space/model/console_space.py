from datetime import datetime
from typing import List

from pydantic import BaseModel

from watchmen.common.watchmen_model import WatchmenModel

from watchmen.common.parameter import ParameterJoint, Parameter
from watchmen.common.watchmen_model import WatchmenModel
from watchmen.report.model.report import Report
from watchmen.topic.topic import Topic


class ConsoleSpaceSubjectChartDataSet(BaseModel):
    meta: List[str] = []
    data: list = []


class SubjectDataSetJoin(BaseModel):
    topicId: str = None
    factorId: str = None
    secondaryTopicId: str = None
    secondaryFactorId: str = None
    type: str = None


class SubjectDataSetFilter(ParameterJoint):
    pass


class SubjectDataSetFilterJoint(ParameterJoint):
    filters: List[SubjectDataSetFilter]


class SubjectDataSetColumn(BaseModel):
    columnId: str = None
    parameter: Parameter
    alias: str = None


class SubjectDataSet(BaseModel):
    filters: SubjectDataSetFilterJoint
    columns: List[SubjectDataSetColumn] = []
    joins: List[SubjectDataSetJoin] = []


class ConsoleSpaceSubject(WatchmenModel):
    subjectId: str = None
    name: str = None
    topicCount: int = None
    graphicsCount: int = None
    lastVisitTime: datetime = None
    createdAt: str = None
    reports: List[Report] = []
    reportIds: list = []
    dataset: SubjectDataSet = None
    tenantId: str = None


class ConsoleSpaceGroup(WatchmenModel):
    groupId: str = None
    name: str = None
    subjects: List[ConsoleSpaceSubject] = []
    subjectIds: list = []
    tenantId: str = None


class ConsoleSpace(WatchmenModel):
    spaceId: str = None
    name: str = None
    connectId: str = None
    type: str = None
    lastVisitTime: datetime = None
    # groups: List[ConsoleSpaceGroup] = []
    subjects: List[ConsoleSpaceSubject] = []
    groupIds: list = []
    subjectIds: list = []
    userId: str = None
    topics: List[Topic] = []
    tenantId: str = None
    # topicRelations: List[TopicRelationship] = []
