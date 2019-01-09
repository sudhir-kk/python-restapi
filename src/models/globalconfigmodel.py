""" src/models/globalconfigmodel.py"""
from . import db
import datetime
from marshmallow import fields, Schema


class GlobalConfigModel(db.Model):
    """ TemplateGroupModel"""
    __tablename__ = 'globalconfig'

    globalConfigId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    globalConfigType = db.Column(db.String(50), nullable=True)
    globalConfigPath = db.Column(db.String(50), nullable=True)
    globalConfigName = db.Column(db.String(50), unique=True, nullable=False)
    globalConfigDefaultValue = db.Column(db.String(50), nullable=True)
    globalConfigFullPath = db.Column(db.String(50), nullable=True)
    globalConfigUuid = db.Column(db.String(50), nullable=True)
    opsCodeAutoId = db.Column(db.String(50), nullable=True)
    globalConfigIsActive = db.Column(db.Boolean(), nullable=False)
    createdBy = db.Column(db.String(50), nullable=True)
    createdOn = db.Column(db.DateTime, nullable=True)
    lastUpdatedBy = db.Column(db.String(50), nullable=True)
    lastUpdatedOn = db.Column(db.DateTime, nullable=True)

    def __init__(self, data):
        self.globalConfigType = data.get('globalConfigType')
        self.globalConfigPath = data.get('globalConfigPath')
        self.globalConfigName = data.get('globalConfigName')
        self.globalConfigDefaultValue = data.get('globalConfigDefaultValue')
        self.globalConfigFullPath = data.get('globalConfigFullPath')
        self.globalConfigUuid = data.get('globalConfigUuid')
        self.opsCodeAutoId = data.get('opsCodeAutoId')
        self.globalConfigIsActive = data.get('globalConfigIsActive')
        self.createdBy = data.get('createdBy')
        self.createdOn = datetime.datetime.utcnow()
        self.lastUpdatedBy = data.get('lastUpdatedBy')
        self.lastUpdatedOn = datetime.datetime.utcnow()

    def save(self, loggeduser):
        """ this is save method"""
        db.session.add(self)
        self.createdBy = loggeduser
        self.lastUpdatedBy = loggeduser
        db.session.commit()

    def update(self, data, loggeduser):
        """ this is update method"""
        for key, item in data.items():
            setattr(self, key, item)
        self.lastUpdatedBy = loggeduser
        self.lastUpdatedOn = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self, data, loggeduser):
        """ this is delete method"""
        for key, item in data.items():
            setattr(self, key, item)
        self.globalConfigIsActive = False
        self.lastUpdatedBy = loggeduser
        self.lastUpdatedOn = datetime.datetime.utcnow()
        db.session.commit()

    def __repr__(self):
        return '<globalConfigId {}>'.format(self.globalConfigId)


class GlobalConfigSchema(Schema):
    """ GlobalConfig  Schema  """
    globalConfigId = fields.Int(dump_only=True)
    globalConfigType = fields.Str(required=False)
    globalConfigPath = fields.Str(required=False)
    globalConfigName = fields.Str(required=True)
    globalConfigDefaultValue = fields.Str(required=False)
    globalConfigFullPath = fields.Str(required=False)
    globalConfigUuid = fields.Str(required=False)
    opsCodeAutoId = fields.Str(required=False)
    globalConfigIsActive = fields.Boolean(required=True)
    """ below attributes will be uncommented when customer needs """
    # createdBy = fields.Str(required=False)
    # createdOn = fields.DateTime(dump_only=True)
    # lastUpdatedBy = fields.Str(required=False)
    # lastUpdatedOn = fields.DateTime(dump_only=True)
