# coding: utf-8

from app.util.clickhouse import ck_client
from collections import namedtuple

BlsElectInfo = namedtuple('BlsElectInfo', ['id', 'elect_height', 'shard_id', 'member_idx', 'contribution_map', 'local_sk', 'common_pk'])

def get_bls_elect_info_list(limit: int = 10, offset: int = 0):
    elect_infos = ck_client.execute('select * from bls_elect_info order by elect_height desc limit 10 offset 0;')
    return [BlsElectInfo(*row) for row in elect_infos]

