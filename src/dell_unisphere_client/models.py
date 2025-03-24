"""Dell Unisphere API Models.

This module provides data models for Dell Unisphere API responses.
"""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional


class UpgradeStatusEnum(str, Enum):
    """Upgrade status enum."""

    UNKNOWN = "Unknown"
    PREPARING = "Preparing"
    PREPARED = "Prepared"
    UPGRADING = "Upgrading"
    UPGRADED = "Upgraded"
    COMMITTING = "Committing"
    COMMITTED = "Committed"
    COMPLETED = "Completed"
    FAILED = "Failed"
    ROLLING_BACK = "RollingBack"
    ROLLED_BACK = "RolledBack"


class UpgradeSessionTypeEnum(str, Enum):
    """Upgrade session type enum."""

    UNKNOWN = "Unknown"
    UPGRADE = "Upgrade"
    ROLLBACK = "Rollback"


class UpgradeTypeEnum(str, Enum):
    """Upgrade type enum."""

    UNKNOWN = "Unknown"
    FIRMWARE = "Firmware"
    SOFTWARE = "Software"
    LANGUAGE_PACK = "LanguagePack"


@dataclass
class Link:
    """API link model."""

    rel: str
    href: str


@dataclass
class ApiResponse:
    """Base API response model."""

    base: str  # Formerly @base
    updated: datetime
    links: List[Link]


@dataclass
class NameValuePair:
    """Name-value pair model."""

    name: str
    value: str


@dataclass
class FirmwarePackage:
    """Firmware package model."""

    name: str
    version: str


@dataclass
class InstalledSoftwareVersionLanguage:
    """Installed software version language model."""

    name: str
    version: str


@dataclass
class InstalledSoftwareVersionPackage:
    """Installed software version package model."""

    name: str
    version: str


@dataclass
class BasicSystemInfo:
    """Basic system info model."""

    id: str
    model: str
    name: str
    softwareVersion: str
    softwareFullVersion: str
    apiVersion: str
    earliestApiVersion: str


@dataclass
class BasicSystemInfoEntry:
    """Basic system info entry model."""

    content: BasicSystemInfo


@dataclass
class BasicSystemInfoResponse:
    """Basic system info response model."""

    base: str
    updated: datetime
    links: List[Link]
    entries: List[BasicSystemInfoEntry]


@dataclass
class InstalledSoftwareVersion:
    """Installed software version model."""

    id: str
    version: str
    fullVersion: str
    isLatest: bool
    releaseDate: datetime
    firmwarePackages: List[FirmwarePackage] = None
    languages: List[InstalledSoftwareVersionLanguage] = None
    packages: List[InstalledSoftwareVersionPackage] = None


@dataclass
class InstalledSoftwareVersionEntry:
    """Installed software version entry model."""

    content: InstalledSoftwareVersion


@dataclass
class InstalledSoftwareVersionResponse:
    """Installed software version response model."""

    base: str
    updated: datetime
    links: List[Link]
    entries: List[InstalledSoftwareVersionEntry]


@dataclass
class CandidateSoftwareVersion:
    """Candidate software version model."""

    id: str
    version: str
    fullVersion: str
    status: str
    type: UpgradeTypeEnum
    isCompatible: bool
    isValid: bool
    fileName: str
    fileSize: int
    uploadTime: datetime
    attributes: List[NameValuePair] = None


@dataclass
class CandidateSoftwareVersionEntry:
    """Candidate software version entry model."""

    content: CandidateSoftwareVersion


@dataclass
class CandidateSoftwareVersionResponse:
    """Candidate software version response model."""

    base: str
    updated: datetime
    links: List[Link]
    entries: List[CandidateSoftwareVersionEntry]


@dataclass
class UpgradeMessage:
    """Upgrade message model."""

    id: str
    severity: str
    message: str
    timestamp: datetime


@dataclass
class UpgradeTask:
    """Upgrade task model."""

    id: str
    caption: str
    creationTime: datetime
    status: UpgradeStatusEnum
    type: UpgradeSessionTypeEnum
    estRemainTime: Optional[str] = None


@dataclass
class SoftwareUpgradeSession:
    """Software upgrade session model."""

    id: str
    description: Optional[str] = None
    status: UpgradeStatusEnum
    type: UpgradeSessionTypeEnum
    upgradeType: UpgradeTypeEnum
    candidateVersionId: str
    candidateVersion: str
    percentComplete: int
    startTime: datetime
    endTime: Optional[datetime] = None
    estRemainTime: Optional[str] = None
    messages: List[UpgradeMessage] = None
    tasks: List[UpgradeTask] = None


@dataclass
class SoftwareUpgradeSessionEntry:
    """Software upgrade session entry model."""

    content: SoftwareUpgradeSession


@dataclass
class SoftwareUpgradeSessionResponse:
    """Software upgrade session response model."""

    base: str
    updated: datetime
    links: List[Link]
    entries: List[SoftwareUpgradeSessionEntry]
