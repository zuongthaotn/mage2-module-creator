<?php
namespace {{namespace}}\{{module_name}}\Model;

use {{namespace}}\{{module_name}}\Api\Data\{{interface_name}}Interface;
use Magento\Framework\App\ObjectManager;
use Magento\Framework\DataObject\IdentityInterface;
use Magento\Framework\Model\AbstractModel;
use Magento\Framework\Validation\ValidationException;
use Magento\Framework\Validator\HTML\WYSIWYGValidatorInterface;
use Magento\Framework\Model\Context;
use Magento\Framework\Registry;
use Magento\Framework\Model\ResourceModel\AbstractResource;
use Magento\Framework\Data\Collection\AbstractDb;
use Magento\Backend\Model\Validator\UrlKey\CompositeUrlKey;
use Magento\Framework\Exception\LocalizedException;

/**
 * {{interface_name}} model
 *
 */
class {{interface_name}} extends AbstractModel implements {{interface_name}}Interface
{

    public const CACHE_TAG = '{{interface_name_lower}}_b';

    /**
     * Prefix of model events names
     *
     * @var string
     */
    protected $_eventPrefix = '{{interface_name_lower}}_prevent';

    /**
     * @param Context $context
     * @param Registry $registry
     * @param AbstractResource|null $resource
     * @param AbstractDb|null $resourceCollection
     * @param array $data
     */
    public function __construct(
        Context $context,
        Registry $registry,
        AbstractResource $resource = null,
        AbstractDb $resourceCollection = null,
        array $data = []
    ) {
        parent::__construct($context, $registry, $resource, $resourceCollection, $data);
    }

    /**
     * Construct.
     *
     * @return void
     */
    protected function _construct()
    {
        $this->_init(\{{namespace}}\{{module_name}}\Model\ResourceModel\{{interface_name}}::class);
    }

    /**
     * Retrieve {{interface_name_lower}} id
     *
     * @return int
     */
    public function getId()
    {
        return $this->getData(self::{{interface_name_upper}}_ID);
    }

    /**
     * Retrieve {{interface_name_lower}} name
     *
     * @return string
     */
    public function getName()
    {
        return $this->getData(self::NAME);
    }

    /**
     * Is enable
     *
     * @return bool
     */
    public function isEnable()
    {
        return (bool)$this->getData(self::IS_ENABLE);
    }

    /**
     * Set ID
     *
     * @param int $id
     * @return {{interface_name}}Interface
     */
    public function setId($id)
    {
        return $this->setData(self::{{interface_name_upper}}_ID, $id);
    }

    /**
     * Set name
     *
     * @param string $name
     * @return {{interface_name}}Interface
     */
    public function setName($name)
    {
        return $this->setData(self::NAME, $name);
    }

    /**
     * Set is enable
     *
     * @param bool|int $isEnable
     * @return {{interface_name}}Interface
     */
    public function setIsEnable($isEnable)
    {
        return $this->setData(self::IS_ENABLE, $isEnable);
    }

    /**
     * Prepare {{interface_name_lower}}'s statuses.
     *
     * @return array
     */
    public function getAvailableStatuses()
    {
        return [self::STATUS_ENABLED => __('Enabled'), self::STATUS_DISABLED => __('Disabled')];
    }
}
