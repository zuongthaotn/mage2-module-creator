<?php
namespace {{namespace}}\{{module_name}}\Model\{{interface_name}};

use {{namespace}}\{{module_name}}\Model\ResourceModel\{{interface_name}}\CollectionFactory;
use Magento\Catalog\Model\Category\FileInfo;
use Magento\Framework\App\ObjectManager;
use Magento\Framework\App\Request\DataPersistorInterface;
use Magento\Store\Model\StoreManagerInterface;
use Magento\Ui\DataProvider\Modifier\PoolInterface;

/**
 * Class DataProvider
 */
class DataProvider extends \Magento\Ui\DataProvider\ModifierPoolDataProvider
{
    /**
     * @var \{{namespace}}\{{module_name}}\Model\ResourceModel\{{interface_name}}\Collection
     */
    protected $collection;

    /**
     * @var DataPersistorInterface
     */
    protected $dataPersistor;

    /**
     * @var array
     */
    protected $loadedData;

    /**
     * @var StoreManagerInterface
     */
    private $storeManager;

    public function __construct(
        $name,
        $primaryFieldName,
        $requestFieldName,
        CollectionFactory ${{interface_name_lower}}CollectionFactory,
        DataPersistorInterface $dataPersistor,
        StoreManagerInterface $storeManager,
        array $meta = [],
        array $data = [],
        PoolInterface $pool = null
    ) {
        $this->collection = ${{interface_name_lower}}CollectionFactory->create();
        $this->dataPersistor = $dataPersistor;
        $this->storeManager = $storeManager;
        parent::__construct($name, $primaryFieldName, $requestFieldName, $meta, $data, $pool);
    }

    /**
     * Get data
     *
     * @return array
     */
    public function getData()
    {
        if (isset($this->loadedData)) {
            return $this->loadedData;
        }
        $items = $this->collection->getItems();
        /** @var \{{namespace}}\{{module_name}}\Model\{{interface_name}} ${{interface_name_lower}} */
        foreach ($items as ${{interface_name_lower}}) {
            $this->loadedData[${{interface_name_lower}}->getId()] = ${{interface_name_lower}}->getData();
        }

        $data = $this->dataPersistor->get('{{interface_name_lower}}_data_persis');
        if (!empty($data)) {
            ${{interface_name_lower}} = $this->collection->getNewEmptyItem();
            ${{interface_name_lower}}->setData($data);
            $this->loadedData[${{interface_name_lower}}->getId()] = ${{interface_name_lower}}->getData();
            $this->dataPersistor->clear('{{interface_name_lower}}_data_persis');
        }
        return $this->loadedData;
    }
}
