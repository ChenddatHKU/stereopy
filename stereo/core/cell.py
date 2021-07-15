#!/usr/bin/env python3
# coding: utf-8
"""
@file: cell.py
@description: 
@author: Ping Qiu
@email: qiuping1@genomics.cn
@last modified by: Ping Qiu

change log:
    2021/06/29  create file.
"""
from typing import Optional

import numpy as np


class Cell(object):
    def __init__(self, cell_name: Optional[np.ndarray] = None):
        self._cell_name = cell_name
        self.total_counts = None
        self.pct_counts_mt = None
        self.n_genes_by_counts = None

    @property
    def cell_name(self):
        return self._cell_name

    @cell_name.setter
    def cell_name(self, name):
        if not isinstance(name, np.ndarray):
            raise TypeError('cell name must be a np.ndarray object.')
        self._cell_name = name

    def sub_set(self, index):
        if self.cell_name is not None:
            self.cell_name = self.cell_name[index]
        if self.total_counts is not None:
            self.total_counts = self.total_counts[index]
        if self.pct_counts_mt is not None:
            self.pct_counts_mt = self.pct_counts_mt[index]
        if self.n_genes_by_counts is not None:
            self.n_genes_by_counts = self.n_genes_by_counts[index]
        return self

    def get_property(self, name):
        if name == 'total_counts':
            return self.total_counts
        if name == 'pct_counts_mt':
            return self.pct_counts_mt
        if name == 'n_genes_by_counts':
            return self.n_genes_by_counts
