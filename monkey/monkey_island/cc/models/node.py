from typing import Mapping, Tuple, TypeAlias

from pydantic import Field, validator

from common.base_models import MutableInfectionMonkeyBaseModel

from . import CommunicationType, MachineID

NodeConnections: TypeAlias = Mapping[MachineID, Tuple[CommunicationType, ...]]


class Node(MutableInfectionMonkeyBaseModel):
    """
    A network node and its outbound connections/communications

    A node is identified by a MachineID and tracks all outbound communication to other machines on
    the network. This is particularly useful for creating graphs of Infection Monkey's activity
    throughout the network.
    """

    machine_id: MachineID = Field(..., allow_mutation=False)
    """The MachineID of the node (source)"""

    connections: NodeConnections
    """All outbound connections from this node to other machines"""
