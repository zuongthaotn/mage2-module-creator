<?php

namespace {{namespace}}\{{module_name}}\Model;

use {{namespace}}\{{module_name}}\Api\{{interface_name}}RepositoryInterface;
use {{namespace}}\{{module_name}}\Api\Data;
use {{namespace}}\{{module_name}}\Model\ResourceModel\{{interface_name}} as Resource{{interface_name}};
use {{namespace}}\{{module_name}}\Model\ResourceModel\{{interface_name}}\CollectionFactory as {{interface_name}}CollectionFactory;
use Magento\Framework\Api\DataObjectHelper;
use Magento\Framework\Api\SearchCriteria\CollectionProcessorInterface;
use Magento\Framework\App\ObjectManager;
use Magento\Framework\Exception\CouldNotDeleteException;
use Magento\Framework\Exception\CouldNotSaveException;
use Magento\Framework\Exception\NoSuchEntityException;
use Magento\Framework\Reflection\DataObjectProcessor;
use Magento\Store\Model\StoreManagerInterface;
use Magento\Framework\EntityManager\HydratorInterface;

/**
 * Default repo impl.
 * @SuppressWarnings(PHPMD.CouplingBetweenObjects)
 */
class {{interface_name}}Repository implements {{interface_name}}RepositoryInterface
{
    /**
     * @var Resource{{interface_name}}
     */
    protected $resource;

    /**
     * @var  {{interface_name}}Factory
     */
    protected ${{interface_name_lower}}Factory;

    /**
     * @var {{interface_name}}CollectionFactory
     */
    protected ${{interface_name_lower}}CollectionFactory;

    /**
     * @var Data\{{interface_name}}SearchResultsInterfaceFactory
     */
    protected $searchResultsFactory;

    /**
     * @var DataObjectHelper
     */
    protected $dataObjectHelper;

    /**
     * @var DataObjectProcessor
     */
    protected $dataObjectProcessor;

    /**
     * @var \{{namespace}}\{{module_name}}\Api\Data\{{interface_name}}InterfaceFactory
     */
    protected $data{{interface_name}}Factory;

    /**
     * @var \Magento\Store\Model\StoreManagerInterface
     */
    private $storeManager;

    /**
     * @var CollectionProcessorInterface
     */
    private $collectionProcessor;

    /**
     * @var HydratorInterface
     */
    private $hydrator;

    /**
     * @param Resource{{interface_name}} $resource
     * @param {{interface_name}}Factory ${{interface_name_lower}}Factory
     * @param Data\{{interface_name}}InterfaceFactory $data{{interface_name}}Factory
     * @param {{interface_name}}CollectionFactory ${{interface_name_lower}}CollectionFactory
     * @param Data\{{interface_name}}SearchResultsInterfaceFactory $searchResultsFactory
     * @param DataObjectHelper $dataObjectHelper
     * @param DataObjectProcessor $dataObjectProcessor
     * @param StoreManagerInterface $storeManager
     * @param CollectionProcessorInterface|null $collectionProcessor
     * @param HydratorInterface|null $hydrator
     */
    public function __construct(
        Resource{{interface_name}} $resource,
         {{interface_name}}Factory ${{interface_name_lower}}Factory,
        \{{namespace}}\{{module_name}}\Api\Data\{{interface_name}}InterfaceFactory $data{{interface_name}}Factory,
        {{interface_name}}CollectionFactory ${{interface_name_lower}}CollectionFactory,
        Data\{{interface_name}}SearchResultsInterfaceFactory $searchResultsFactory,
        DataObjectHelper $dataObjectHelper,
        DataObjectProcessor $dataObjectProcessor,
        StoreManagerInterface $storeManager,
        CollectionProcessorInterface $collectionProcessor = null,
        ?HydratorInterface $hydrator = null
    ) {
        $this->resource = $resource;
        $this->{{interface_name_lower}}Factory = ${{interface_name_lower}}Factory;
        $this->{{interface_name_lower}}CollectionFactory = ${{interface_name_lower}}CollectionFactory;
        $this->searchResultsFactory = $searchResultsFactory;
        $this->dataObjectHelper = $dataObjectHelper;
        $this->data{{interface_name}}Factory = $data{{interface_name}}Factory;
        $this->dataObjectProcessor = $dataObjectProcessor;
        $this->storeManager = $storeManager;
        $this->collectionProcessor = $collectionProcessor;
        $this->hydrator = $hydrator ?? ObjectManager::getInstance()->get(HydratorInterface::class);
    }

    /**
     * Save {{interface_name_lower}} data
     *
     * @param \{{namespace}}\{{module_name}}\Api\Data\{{interface_name}}Interface ${{interface_name_lower}}
     * @return {{interface_name}}
     * @throws CouldNotSaveException
     */
    public function save(Data\{{interface_name}}Interface ${{interface_name_lower}})
    {
        if (${{interface_name_lower}}->getId() && ${{interface_name_lower}} instanceof {{interface_name}} && !${{interface_name_lower}}->getOrigData()) {
            ${{interface_name_lower}} = $this->hydrator->hydrate($this->getById(${{interface_name_lower}}->getId()), $this->hydrator->extract(${{interface_name_lower}}));
        }
        try {
            $this->resource->save(${{interface_name_lower}});
        } catch (\Exception $exception) {
            throw new CouldNotSaveException(__($exception->getMessage()));
        }
        return ${{interface_name_lower}};
    }

    /**
     * Load {{interface_name_lower}} data by given {{interface_name_lower}} Identity
     *
     * @param string ${{interface_name_lower}}Id
     * @return {{interface_name_lower}}
     * @throws \Magento\Framework\Exception\NoSuchEntityException
     */
    public function getById(${{interface_name_lower}}Id)
    {
        ${{interface_name_lower}} = $this->{{interface_name_lower}}Factory->create();
        $this->resource->load(${{interface_name_lower}}, ${{interface_name_lower}}Id);
        if (!${{interface_name_lower}}->getId()) {
            throw new NoSuchEntityException(__('The {{interface_name_lower}} with the "%1" ID doesn\'t exist.', ${{interface_name_lower}}Id));
        }
        return ${{interface_name_lower}};
    }

    /**
     * Load {{interface_name_lower}} data collection by given search criteria
     *
     * @SuppressWarnings(PHPMD.CyclomaticComplexity)
     * @SuppressWarnings(PHPMD.NPathComplexity)
     * @param \Magento\Framework\Api\SearchCriteriaInterface $criteria
     * @return \{{namespace}}\{{module_name}}\Api\Data\{{interface_name}}SearchResultsInterface
     */
    public function getList(\Magento\Framework\Api\SearchCriteriaInterface $criteria)
    {
        /** @var \{{namespace}}\{{module_name}}\Model\ResourceModel\{{interface_name}}\Collection $collection */
        $collection = $this->{{interface_name_lower}}CollectionFactory->create();

        $this->collectionProcessor->process($criteria, $collection);

        /** @var Data\{{interface_name}}SearchResultsInterface $searchResults */
        $searchResults = $this->searchResultsFactory->create();
        $searchResults->setSearchCriteria($criteria);
        $searchResults->setItems($collection->getItems());
        $searchResults->setTotalCount($collection->getSize());
        return $searchResults;
    }

    /**
     * Delete {{interface_name_lower}}
     *
     * @param \{{namespace}}\{{module_name}}\Api\Data\{{interface_name}}Interface ${{interface_name_lower}}
     * @return bool
     * @throws CouldNotDeleteException
     */
    public function delete(Data\{{interface_name}}Interface ${{interface_name_lower}})
    {
        try {
            $this->resource->delete(${{interface_name_lower}});
        } catch (\Exception $exception) {
            throw new CouldNotDeleteException(__($exception->getMessage()));
        }
        return true;
    }

    /**
     * Delete {{interface_name_lower}} by given {{interface_name_lower}} Identity
     *
     * @param string ${{interface_name_lower}}Id
     * @return bool
     * @throws CouldNotDeleteException
     * @throws NoSuchEntityException
     */
    public function deleteById(${{interface_name_lower}}Id)
    {
        return $this->delete($this->getById(${{interface_name_lower}}Id));
    }
}
