"""Basic download function."""

from kghub_downloader.download_utils import download_from_yaml  # type: ignore


def download(yaml_file: str, output_dir: str, ignore_cache: bool = False) -> None:
    """Download data files from list of URLs into data directory.

    Args:
        yaml_file: A string pointing to the yaml file utilized
        to facilitate the downloading of data.
        output_dir: A string pointing to the location to download data to.
        ignore_cache: Ignore cache and download files even if they exist [false]

    Returns:
        None.
    """
    download_from_yaml(
        yaml_file=yaml_file, output_dir=output_dir, ignore_cache=ignore_cache
    )

    return None
