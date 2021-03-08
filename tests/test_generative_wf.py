import logging

from tests.utils import _create_context

from nvidia.cheminformatics.wf.generate.latentspaceinterpolation import LatentSpaceInterpolation
from nvidia.cheminformatics.decorator import LipinskiRuleOfFiveDecorator, MolecularStructureDecorator


logger = logging.getLogger(__name__)


def test_latent_space_interpolation():
    """
    Verify fetching data from chemblDB when the input is a pandas df.
    """
    num_points = 10
    context = _create_context()
    wf = LatentSpaceInterpolation()

    smiles = ['CHEMBL263882', 'CHEMBL7214']
    genreated_df = wf.interpolate_from_id(smiles, num_points=num_points)

    logger.info(genreated_df.head(10))
    assert genreated_df.shape[0] == num_points

    genreated_df = MolecularStructureDecorator().decorate(genreated_df)
    genreated_df = LipinskiRuleOfFiveDecorator().decorate(genreated_df)

    logger.info(genreated_df.head(20))

    logger.info(genreated_df.columns)
    logger.info(genreated_df.columns.to_list())