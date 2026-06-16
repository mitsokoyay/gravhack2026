from csv_writer import csv_writer


def test_open_writes_header_once(tmp_path):
    out = tmp_path / "data.csv"

    logger = csv_writer(str(out), headers=["timestamp", "raw_data"])
    logger.open()
    logger.close()

    # Re-open: header should NOT be duplicated
    logger = csv_writer(str(out), headers=["timestamp", "raw_data"])
    logger.open()
    logger.close()

    lines = out.read_text(encoding="utf-8").splitlines()
    assert lines == ["timestamp,raw_data"]


def test_write_raw_adds_timestamp_and_data(tmp_path):
    out = tmp_path / "data.csv"

    logger = csv_writer(str(out))
    logger.open()
    logger.write_raw("hello")
    logger.close()

    lines = out.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "timestamp,raw_data"
    assert len(lines) == 2
    assert lines[1].endswith(",hello")  # timestamp is variable


def test_write_row_writes_exact_row(tmp_path):
    out = tmp_path / "data.csv"

    logger = csv_writer(str(out), headers=["c1", "c2"])
    logger.open()
    logger.write_row(["a", "b"])
    logger.close()

    lines = out.read_text(encoding="utf-8").splitlines()
    assert lines == ["c1,c2", "a,b"]
